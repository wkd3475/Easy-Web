<template>
  <div id="app">
    <el-container style="height: 700px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <MainSidebar />
      </el-aside>
      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <MainHeader />
        </el-header>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import MainHeader from './components/Layout/MainHeader.vue'
import MainSidebar from './components/Layout/MainSidebar.vue'
export default {
  name: 'App',
  components: {
    MainHeader,
    MainSidebar,
  }
}
</script>