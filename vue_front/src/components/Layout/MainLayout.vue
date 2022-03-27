<template>
<el-container style="height: 700px; border: 1px solid #eee">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
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
  </el-aside>

  <el-container>
    <el-header style="text-align: right; font-size: 12px">
      <el-dropdown>
        <i class="el-icon-setting" style="margin-right: 15px"></i>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>View</el-dropdown-item>
          <el-dropdown-item>Add</el-dropdown-item>
          <el-dropdown-item>Delete</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <span>Tom</span>
    </el-header>
    
    <el-main>
      <el-table :data="tableData">
        <el-table-column prop="date" label="Date" width="140">
        </el-table-column>
        <el-table-column prop="name" label="Name" width="120">
        </el-table-column>
        <el-table-column prop="address" label="Address">
        </el-table-column>
      </el-table>
    </el-main>
  </el-container>
</el-container>
</template>
<style>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  
  .el-aside {
    color: #333;
  }
</style>

<script>
  export default {
    name: 'MainLayout',
    data() {
      const item_list = [
        {
          date: '2016-05-02',
          name: 'Tom',
          address: 'No. 189, Grove St, Los Angeles'
        },
        {
          date: '2022-05-02',
          name: 'Abc',
          address: 'No. 18sdafasdfAngeles'
        },
      ];
      // const item = {
      //   date: '2016-05-02',
      //   name: 'Tom',
      //   address: 'No. 189, Grove St, Los Angeles'
      // };
      return {
        tableData: item_list
      }
    }
  };
</script>