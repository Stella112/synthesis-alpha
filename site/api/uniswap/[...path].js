export default async function handler(req, res) {
  // Extract the path after /api/uniswap/
  const { path } = req.query;
  const targetPath = Array.isArray(path) ? path.join('/') : path;
  const targetUrl = `https://trade-api.gateway.uniswap.org/${targetPath}`;

  try {
    const response = await fetch(targetUrl, {
      method: req.method,
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': req.headers['x-api-key'] || '',
        'x-universal-router-version': req.headers['x-universal-router-version'] || '2.0',
      },
      body: req.method === 'POST' ? JSON.stringify(req.body) : undefined,
    });

    const data = await response.json();
    res.status(response.status).json(data);
  } catch (error) {
    console.error('Uniswap proxy error:', error);
    res.status(500).json({ error: 'Proxy request failed' });
  }
}
