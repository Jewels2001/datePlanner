<script setup>
import { ref } from 'vue'
// import TextBox from './TextBox.vue'
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'

let request;
const message1 = ref('')
const message2 = ref('')
const placeType = ref([])
var arr = []

// let examplesDropdown = ref('');

function send() {
  let m1 = `${message1.value}`
  let m2 = `${message2.value}`
  let m3 = `${placeType.value}`
  console.log(m1)
  console.log(m2)
  console.log(m3)
  this.arr.push({ first: m1, second: m2, third: m3});
  console.log(1);
  const data = JSON.stringify(this.arr)
  window.localStorage.setItem('arr', data);
  console.log(JSON.parse(window.localStorage.getItem('arr')))
   
}

</script>

<template>
 <div class="grid justify-center place-content-center">
  
  <div><p>This is the rest of the webpage</p></div>
  <div class="box"> 
    <h2> 1 box </h2>
        <div>
      <input class="textInput1" v-model="message1" placeholder= "Location" />
      </div>
    <!-- <TextBox :place="Food" /> -->
  </div>
    <div class="box"> 2 box
          <div>
          <!-- <p>Message is: {{ message }}</p> -->
      <input class="textInput1" v-model="message2" placeholder= "Activites" />
      </div>
      <!-- <TextBox :place="Location" /> -->
    </div>
    <div class="box text-red-500">
      <select v-model="placeType" multiple>
      <option> Restaurants</option>
      <option> Bars</option>
      <option> Parks</option>
      <option> Recreation</option>
    </select>
    </div>
    <div class="box"> 3 box
            <div>
            <!-- <p>Message is: {{ message }}</p> -->
           <button class="button1" @click="send()">click me</button>
        </div>
        <!-- <TextBox :place="Location" /> -->
      </div>


 </div>
</template>

<style>
.box { 
  @apply rounded border-s-4 border-2 border-red-400 p-2 m-4 flex-col text-center max-w-sm
  /* place-content-center divide-y  */
}
.textInput1 {
    @apply rounded border-2 w-full placeholder:italic placeholder:p-2 text-red-600 p-1
}

.button1 {
  @apply border border-red-400 rounded-full p-2 m-4
}

</style>
