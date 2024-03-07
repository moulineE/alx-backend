import { createClient } from 'redis';
import { promisify } from 'util';
import express from 'express';
const kue = require('kue');
const queue = kue.createQueue();
const app = express();
const port = 1245;
let reservationEnabled;

const client = createClient()
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'));

function reserveSeat (number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats () {
  const getAsync = promisify(client.get).bind(client);
  return await getAsync('available_seats');
}

app.get('/available_seats', async (req, res) => {
  const availSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }
  const job = queue.create('reserve_seat').save(err => {
    if (!err) res.json({ status: 'Reservation in process' });
    if (err) res.json({ status: 'Reservation failed' });
  });
  job
    .on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    })
    .on('failed', (errorMessage) => {
      console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    });
});

app.get('/process', async (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    let availSeats = await getCurrentAvailableSeats();
    availSeats = Number(availSeats);
    if (availSeats === 0) {
      done(new Error('Not enough seats available'));
      return;
    }
    const newAvailSeats = availSeats - 1;
    reserveSeat(newAvailSeats);
    if (newAvailSeats === 0) {
      reservationEnabled = false;
    }
    done();
  });
  res.json({ status: 'Queue processing' });
});

app.listen(port, () => {
  reserveSeat(50);
  reservationEnabled = true;
  console.log(`Example app listening on port ${port}`);
});
