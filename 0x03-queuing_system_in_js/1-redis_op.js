import { createClient, print } from 'redis';

const client = createClient()
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'));

async function setNewSchool (schoolName, value) {
  await client.set(schoolName, value, print);
}

async function displaySchoolValue (schoolName) {
  await client.get(schoolName, (_err, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
