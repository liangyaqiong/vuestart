<template>
  <el-table
    :data="info"
    border
    style="width: 100%">
    <el-table-column
      prop="name"
      label="元素名"
      width="160">
    </el-table-column>
    <el-table-column
      prop="page"
      label="页面"
      width="120">
    </el-table-column>
    <el-table-column
      prop="component"
      label="组件"
      width="120">
    </el-table-column>
    <el-table-column
      prop="find_by"
      label="定位方式"
      width="100">
    </el-table-column>
    <el-table-column
      prop="value"
      label="定位值"
      width="100">
    </el-table-column>
      <el-table-column
      prop="insert_time"
      label="新增时间"
      width="120">
    </el-table-column>
      </el-table-column>
      <el-table-column
      prop="update_time"
      label="更新时间"
      width="120">
    </el-table-column>
        <el-table-column
      prop="parent_find_by"
      label="父元素定位方式"
      width="140">
    </el-table-column>
       <el-table-column
      prop="parent_value"
      label="父元素定位值"
      width="180">
    </el-table-column>
     <el-table-column
      prop="description"
      label="描述"
      width="120">
    </el-table-column>
    <el-table-column
      fixed="right"
      label="操作"
      width="100">
      <template slot-scope="scope">
        <el-button @click="handleClick(scope.row)" type="text" size="small">删除</el-button>
        <el-button type="text" size="small">编辑</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
//导出组件
export default {
  name: 'Element',
  methods: {
    queryList () {
      this.$axios
      .get('http://localhost:8000/testqueryall/')
      .then((response) => {
         //iterm把每一个元素进行遍历，map()会将iterm遍历的元素重新append成一个list返回
         const list = response.data.map(function (item) {
           console.log('item===', item)
           //... 展开符
           return {
              ...item, //将最外面层元素保留/copy的新的list
              ...item.fields //将内层元素展开append到list,只能一层一层展开
           }
         })
         console.log('=====', list)
         this.info = list
        })
      .catch(function (error) { // 请求失败处理
        console.log(error)
      })
    },
    handleClick(row) {
       this.$axios
        .get('http://localhost:8000/testdelete/?id='+row.pk)
      .then((response) => {
         this.$message({
          showClose: true,
          message: '恭喜你，这是一条成功消息',
          type: 'success'
        });
        this.queryList()
        })
      .catch(function (error) { // 请求失败处理
        console.log(error)
      })
        console.log(row);
    }
  },
   data() {
      return {
          info:null
        }
      },
  // mounted是生命周期函数，页面渲染成功之后自动执行
	mounted () {
    this.queryList()
}
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
