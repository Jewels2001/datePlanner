<script setup>
import { ref } from 'vue'

const message = ref('')
const place = ref('')

// defineProps({
//     place: {
//         type: String,
//         required: true
//     }
// })

</script>

<template>
    <div>
        <!-- <p>Message is: {{ message }}</p> -->
    <input class="textInput1" v-model="message" :placeholder= "placeholder" />
    </div>
</template>

<style scoped>
.textInput1 {
    @apply rounded border-2 w-full
}
</style>
