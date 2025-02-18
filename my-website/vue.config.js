const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: 'http://backend:5000' // 讓 Vue API 請求 Flask 服務
  }
})
