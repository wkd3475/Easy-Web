<template>
  <div>
    <el-menu :default-openeds="['1']">
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-notebook-2"></i>Study</template>
        <el-menu-item-group>
          <template slot="title">Algorithm</template>
          <el-menu-item index="1-1-1">DP</el-menu-item>
          <el-menu-item index="1-1-2">BFS/DFS</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group>
          <template slot="title">Web</template>
          <el-menu-item index="1-2-1">Backend</el-menu-item>
          <el-menu-item index="1-2-2">Frontend</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-menu"></i>Archive</template>
        <el-menu-item-group>
          <template slot="title">Picture</template>
          <el-menu-item index="2-1-1">Toori</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
    </el-menu>
  </div>
</template>
<script>
  export default {
    name: 'MainSidebar',
  };
</script>
<style>
  .el-aside {
    color: #333;
  }
</style>