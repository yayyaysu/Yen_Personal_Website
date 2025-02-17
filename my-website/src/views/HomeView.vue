<template>
  <div>
    <h1>Flask API 資料</h1>
    <ul>
      <li v-for="item in items" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>

  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import { ref, onMounted } from 'vue';
import api from '@/api/api'; // 引入 api.js

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  setup() {
    const items = ref([]);

    // 取得 Flask API 的資料
    const fetchData = async () => {
      try {
        const response = await api.get('/data');
        items.value = response.data;
      } catch (error) {
        console.error('獲取資料失敗:', error);
      }
    };

    onMounted(fetchData);

    return { items };
  },
};
</script>
