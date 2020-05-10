<template>
  <div>
    <Myheader></Myheader>
    <div class="container">
      <div class="row">
        <div v-for="(articles, key) in getData" class="col">
          <ul>
            <h2>{{key}}</h2>
            <li v-for="article in articles">
              <a :href="article[0]">
                <span class="article">{{article[1]}}</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Myheader from "./header";
export default {
  name: "mainPage",
  components: { Myheader },
  data() {
    return {
      articles: {},
      keys: [],
      interval: null
    };
  },
  methods:{
    loadData(){
      this.interval = setInterval(()=>{
        this.$store.dispatch("GET_DATA");
      }, 120000) // This function makes request to API every 120 seconds
    }
  },
  mounted() {
    this.$store.dispatch("GET_DATA");
    this.loadData();
  },
  computed: {
    getData() {
      return this.$store.getters.GET_DATA_FROM_STORE;
    }
  },
  beforeDestroy(){
    clearInterval(this.interval) 
  }
};
</script>
<style>
.container {
  margin: 0 auto;
  max-width: 2000px;
}

.col{
  max-width: 33%;
}
a {
  text-decoration: none;
  color: black;
}
li {
  list-style: none;
}

.article {
  display: inline-block;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
  white-space: nowrap;
}
</style>