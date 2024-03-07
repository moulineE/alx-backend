import { createClient } from 'redis';
import { promisify } from 'util';
const express = require('express');
const app = express();
const port = 1245;

const client = createClient()
  .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
  .on('connect', () => console.log('Redis client connected to the server'));

const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

function getItemById (id) {
  return listProducts.find((item) => item.Id === id);
}

app.get('/list_products', (req, res) => {
  res.json(listProducts.map((item) => ({
    itemId: item.Id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock
  })));
});

app.get('/list_products/:itemId(\\d+)', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (item === undefined) {
    res.json({ status: 'Product not found' });
    return;
  }
  const redisStock = await getCurrentReservedStockById(itemId);
  res.json({
    itemId: item.Id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: redisStock === null ? item.stock : Number(redisStock)
  });
});

app.get('/reserve_product/:itemId(\\d+)', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (item === undefined) {
    res.json({ status: 'Product not found' });
    return;
  }
  const redisStock = await getCurrentReservedStockById(itemId);
  const currentStock = redisStock === null ? item.stock : Number(redisStock);
  if (currentStock < 1) {
    res.json({ status: 'Not enough stock available', itemId: item.Id });
    return;
  }
  reserveStockById(item.Id, currentStock - 1);
  res.json({ status: 'Reservation confirmed', itemId: item.Id });
});

function reserveStockById (itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById (itemId) {
  const getAsync = promisify(client.get).bind(client);
  return await getAsync(`item.${itemId}`);
}

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
