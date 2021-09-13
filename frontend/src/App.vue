<template>
  <div id="app">
    <el-container style="height: 500px; border: 1px solid #eee">
   <el-header style="font-size: 16px;">
      <el-row>
         <el-col :span="16" style="text-align: left;">
             <span class='el-icon-s-home'>&nbsp&nbsp&nbsp国际化测试天团</span>
         </el-col>
         <el-col :span="8" style="text-align: right;">
             <el-dropdown>
                <i class="el-icon-setting" style="margin-right: 30px"></i>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item>查看</el-dropdown-item>
                  <el-dropdown-item>新增</el-dropdown-item>
                  <el-dropdown-item>删除</el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
         </el-col>
      </el-row>
    </el-header>
    <el-container>
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu :default-openeds="['1', '2']">
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-s-promotion"></i>UI自动化管理</template>
        <el-menu-item-group>
         <el-menu-item index="1-1"><router-link to="/Element" style="text-decoration:none;">元素信息管理</router-link></el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-menu"></i>人人参与</template>
        <el-menu-item-group >
          <el-menu-item index="2-1" class='el-icon-user-solid'><router-link to="/HelloWorld" style="text-decoration:none;">文影</router-link></el-menu-item>
          <el-menu-item index="2-2" class='el-icon-user-solid'><router-link to="/Test" style="text-decoration:none;">静静</router-link></el-menu-item>
          <el-menu-item index="2-3" class='el-icon-user-solid'>满英</el-menu-item>
          <el-menu-item index="2-4" class='el-icon-user-solid'>志鸿</el-menu-item>
          <el-menu-item index="2-5" class='el-icon-user-solid'>小颖</el-menu-item>
          <el-menu-item index="2-6" class='el-icon-user-solid'>红英</el-menu-item>
          <el-menu-item index="2-7" class='el-icon-user-solid'>娜娜</el-menu-item>
          <el-menu-item index="2-8" class='el-icon-user-solid'>林峰</el-menu-item>
          <el-menu-item index="2-9" class='el-icon-user-solid'>王岚</el-menu-item>

        </el-menu-item-group>
        </el-submenu>
      </el-submenu>
    </el-menu>
  </el-aside>
    <el-main>
      <!-- 路由出口 -->
      <!-- 路由匹配到的组件将渲染在这里 -->
       <router-view />
    </el-main>
  </el-container>
</el-container>
  </div>
</template>

<script>
export default {
  name: 'App',
   data() {
      return {

      };
    },
    methods: {

    }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.el-header {
        background-color: #B3C0D1;
        color: #333;
        line-height: 60px;
      }

      .el-aside {
        color: #333;
      }
</style>
