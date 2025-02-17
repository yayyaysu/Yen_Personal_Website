<template>
  <div>
    <h1>Photos</h1>
    <ul>
      <li v-for="photo in photos" :key="photo.id">{{ photo.title }}</li>
    </ul>
  </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'HelloVue',
    data() {
      return {
        photos: [],
      };
    },

    async created() {
      const response = await axios.get('https://jsonplaceholder.typicode.com/photos?_limit=5');
      this.photos = response.data;
    },
  };
  </script>
  
  <style scoped>
  h1 {
    color: #42b983;
  }
  </style>
  