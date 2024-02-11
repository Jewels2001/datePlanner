<script setup>
defineProps({
    msg: {
        type: String,
        required: true
    }
})
</script>

<template>
    <div class="top inset-x-0 top-0 flex justify-between">
        <div class="float-right order-first">
            <h1 class="text-red-300 text-xl">DatePlanner</h1>
        </div>
        <!-- <div class="center grow">

        </div> -->
        <div class="big-logo right-0 float-left gap-x-4 justify-between">
            <h3>Right side</h3>
            <h3>About ?</h3>
            <h3>Other</h3>
        </div>
    </div>
    
</template>

<style scoped>
.top {
  height: 50px;
  overflow: hidden;

}
.big-logo {
   display: flex;
   margin: 2;
}
</style>
