<template>
  <div class="sider" ref="sider">
      <div
          v-for="(token, index) of headers"
          :key="token.id"
          @click="clickItem(token, index)"
          :style="{ 'margin-left': (token.type*0.8) + 'rem' }"
          class="sider-item"
      >
        <p>{{ token.name }}</p>
      </div>
  </div>
</template>


<script>
import md from '@/markdownParser';

export default {
  name: "markdownTOC",
  data(){
    return{
      mdfiel: '',
      headers: '',
      currentHeaderIndex: null,
    }
  },
  props: {
    markdown: null,
    tocx:null,
    tocy:null
  },
  watch:{
    markdown(){
     const tokens = md.parse(this.markdown,{});
     const headers = tokens.filter(token => token.type === 'heading_open');
     console.log(headers);
     let headerList=[];     //define a header list to contain parsed headers
      for (let headerToken of headers) {
        let header = {};
        header.id = headerToken.attrs[0][1];
        header.type = Number(headerToken.tag.substr(1,1));    //  decide if it is a h1/h2/h3/h4 header
        header.name = decodeURIComponent(headerToken.attrs[0][1]);    // copied code, from https://flik1337.com/blog/dev-vue-static-blog/#%E6%B8%B2%E6%9F%93%E6%96%87%E7%AB%A0%E7%9B%AE%E5%BD%95%E6%A0%91
        headerList.push(header);
      }
     console.log(headerList);
      this.headers = headerList;
    },
  },
  methods:{
    clickItem(item, index){
      this.currentHeaderIndex = index;
      this.$emit("clickItem", { item, index });
      // this.scrollTo(item.id);
    },
  },
}
</script>

<style scoped>
.sider{
  position: sticky;

  padding: 15px;
  /*float: left;*/
  width:20%;
  background-color: #fff;
  border-radius: 10px;
  margin-top: 3vh;
  font-size: 0.8rem;
  align-items: stretch;

}
.sider-item {
  border-left: 0.2rem solid #04293A;
  margin: 0;
  padding: 5px;
  overflow: hidden;
}

.sider-item:first-child {
  border-left: none;
}
</style>