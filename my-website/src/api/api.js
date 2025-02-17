import axios from 'axios';

// 設定 Flask 伺服器的 URL
const API_BASE_URL = 'http://127.0.0.1:5000/api/data ';  // Flask 後端 API 位置

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 5000,  // 設定請求超時時間（5 秒）
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
