import { createClient, print } from 'redis';

const util = require('util');

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server:', err.message));
// client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, print);
}

const displaySchoolValue = async (schoolName) => {
  console.log(await util.promisify(client.GET).bind(client)(schoolName));
};
async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
