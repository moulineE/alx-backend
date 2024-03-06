import { createClient, print } from 'redis';

const client = createClient()
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'));

client.HSET('HolbertonSchools', 'Portland', 50, print);
client.HSET('HolbertonSchools', 'Seattle', 80, print);
client.HSET('HolbertonSchools', 'New York', 20, print);
client.HSET('HolbertonSchools', 'PorBogota', 20, print);
client.HSET('HolbertonSchools', 'Cali', 40, print);
client.HSET('HolbertonSchools', 'Paris', 2, print);

client.HGETALL('HolbertonSchools', (_err, reply) => {
  console.log(reply);
});
