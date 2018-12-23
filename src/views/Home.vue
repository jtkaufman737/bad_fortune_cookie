<template>
  <div class="home">
   <div class="center">
    <Home msg="bad fortune cookie"/>
    <img src="https://i.imgur.com/XEdyPYZ.png">
      <center>
        <button @click="getFortune()" class="button">GIVE ME A FORTUNE</button>
        <br/><br/><br/><br/>
        <div v-if="Object.keys(this.fortune).length > 1">
          {{ fortune.fortune }} <br/><br/>
          - {{ fortune.author }}<br/><br/><br/><br/>
          Tags: <span class="tag"> {{ fortune.genre }}</span>
        </div>
      </center>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import Home from '@/components/Home.vue'

export default {
  name: 'home',

  data() {
    return {
      fortune: {},
    }
  },

  components: {
    Home
  },

  methods: {
    getFortune: function () {
      axios({
        method:'get',
        url:'https://cors-escape.herokuapp.com/https://bad-fortune-cookie.herokuapp.com/fortunes/',
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': '*'
        }
      }).then(res => {
        console.log(res.data.results.length)
        let results = res.data.results;
        this.fortune = results[Math.floor(Math.random() * results.length)]
      })
    }
  }

}
</script>
<style>
img {
  height:350px;
}

button {
  color:white;
  background-color:black;
  padding:15px;
  align-self:center;
  border-radius:5px;
  font-size:20px;
}

div.center {
  display:block;
  text-align:center;
  align-items: center;
}
</style>
