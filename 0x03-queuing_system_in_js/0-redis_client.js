import { createClient } from 'redis';

async function run() {
  const client = createClient();

  client.on('error', err => console.log('Redis client not connected to the server:', err.message));
  client.on('connect', () => console.log('Redis client connected to the server'));

//   client.set('Holberton', 'School');
//   client.get('Holberton', (err, reply) => {
//     if (err) {
//       console.log('Get Error:', err);
//       return;
//     }
//     console.log('Get Reply:', reply);
//   });

//   await client.quit();
}

// run().catch(console.error);
