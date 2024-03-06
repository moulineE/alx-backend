import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient()
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'));

async function setNewSchool (schoolName, value) {
  await client.set(schoolName, value, print);
}

async function displaySchoolValue (schoolName) {
  const getAsync = promisify(client.get).bind(client);
  console.log(await getAsync(schoolName));
}

async function main () {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

main();
