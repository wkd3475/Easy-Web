<template>
  <div>
		<el-dropdown>
			<i class="el-icon-setting" style="margin-right: 15px"></i>
			<el-dropdown-menu slot="dropdown">
				<el-dropdown-item>View</el-dropdown-item>
				<el-dropdown-item>Add</el-dropdown-item>
				<el-dropdown-item>Delete</el-dropdown-item>
			</el-dropdown-menu>
		</el-dropdown>
	<span>Toori</span>
	</div>
</template>
<script>
  export default {
    name: 'MainHeader',
  };
</script>
<style>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
</style>