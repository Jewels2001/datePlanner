<script setup>
import TextBox from './TextBox.vue'
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
</script>

<template>
 <div class="grid justify-center place-content-center">
  
  <p>This is the rest of the webpage</p>
  <div class="box"> 
    <h2> 1 box </h2>
    <TextBox :place="Food" />
  </div>
    <div class="box"> 2 box
      <TextBox :place="Location" />
    </div>
 </div>
</template>

<style>
.box { 
  @apply rounded border-s-4 border-2 border-red-400 p-2 m-4 flex-col text-center max-w-sm
  /* place-content-center divide-y  */
}

</style>
