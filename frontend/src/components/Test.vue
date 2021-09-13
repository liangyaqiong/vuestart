<template>
  <div id = 'hu'>
	 <ul>
		 <li v-for='iterm in name'>姓名：{{iterm}}</li>
	 </ul>
		 <hr/>
	 <ul>
		 <li v-for='value in info'>元素名：{{value.fields.name}},&nbsp;&nbsp;&nbsp组件名：{{value.fields.component}}</li>
	 </ul>
	    <hr/>
    </div>
</template>

<script>
//导出组件
export default {
  name: 'Test',
  data() {
    return {
       name:['小明','小强','小芳','小颖','小狗'],
		   info:null,
		}
    },
     // mounted是生命周期函数，页面渲染成功之后自动执行
    mounted () {
      this.elementQuery()
    },
    methods:{
        elementQuery:function(){
        this.$axios
       .get('http://localhost:8000/testquery/')
        //接口调用完成之后的处理
		   .then((response) => {
			  console.log(response);
			  this.info = response.data
	      console.log('------',this.info);

		  })
		  .catch(function (error) {
			console.log(error);
  })
  }
    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
