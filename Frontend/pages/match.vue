<template>
    <div class="h-screen w-screen bg-background1">
        <div v-for="q in questions" class="text-white">
            {{ q["question"] }}
        </div>
    </div>
</template>

<script setup>
const questions = ref([])

onMounted(async() => {
    let qs = await $fetch("http://localhost:8000/entry/questions")
    questions.value = qs.questions
})
</script>