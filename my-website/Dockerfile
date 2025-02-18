# 1. 使用 Node.js 16 作為基礎映像
FROM node:16-alpine AS build

# 2. 設定工作目錄
WORKDIR /app

# 3. 複製 package.json 並安裝依賴
COPY package.json package-lock.json ./
RUN npm install

# 4. 複製所有 Vue 檔案並執行打包
COPY . .
RUN npm run build

# 5. 使用 Nginx 作為靜態文件伺服器
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

# 6. 對外暴露 Nginx 的 80 端口
EXPOSE 80

# 7. 啟動 Nginx
CMD ["nginx", "-g", "daemon off;"]
