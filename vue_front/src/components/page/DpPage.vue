<template>
  <div>
    <el-main>
      <el-table :data="tableData">
        <router-view></router-view>
        <el-table-column prop="date" label="Date" width="140">
        </el-table-column>
        <el-table-column prop="name" label="Name" width="120">
        </el-table-column>
        <el-table-column prop="address" label="Address">
        </el-table-column>
      </el-table>
    </el-main>
  </div>
</template>
<script>
  export default {
    name: 'DpPage',
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
      return {
        tableData: item_list
      }
    }
  };
</script>