<template>
    <div class="w-screen min-h-screen h-fit pb-40 bg-background1 flex items-center flex-col gap-y-10 overflow-y-hidden">
        <h1 class="text-white text-center text-5xl font-lexend pt-20">Your Result</h1>
        <div v-if="userData" class="w-[50vw] min-w-[300px] flex-wrap h-fit flex justify-center items-center flex-col gap-y-20">
            <div class="text-white text-2xl font-urbanist flex flex-col gap-y-4">
                <p class="text-center">Hello {{ userData["firstname"] }} {{ userData["lastname"] }}, welcome to Opp Match 😈‼️</p>
                <p class="text-center">Based on our analysis, we conclude:</p>
            </div>
            <div class="w-full flex flex-col justify-around gap-y-10 text-white font-urbanist text-xl">
                <div class="w-full flex justify-around flex-row flex-wrap">
                    <div>
                        <label class="font-lexend text-2xl">Estimated MBTI:</label>
                        <h2 class="font-lexend text-6xl ml-7 p-2 text-secondary">{{ userData["mbti"] }}</h2>
                    </div>
                    <div class="flex justify-center items-center flex-col">
                        <label class="font-lexend text-2xl">Uniqueness Score:</label>
                        <h2 class="font-lexend text-6xl pt-2 text-secondary">{{ userData["score"] }}</h2>
                        <h2 class="font-lexend text-2xl ml-14 text-white">/10000</h2>
                        <p class="font-urbanist text-sm p-2 text-white">{{ scoreComment(userData["score"]) }}</p>
                    </div>
                </div>
                <div class="w-full flex justify-center flex-col gap-y-10">
                    <div class="w-full flex flex-col gap-y-5">
                        <h2 class="font-lexend text-3xl text-center">Summary</h2>
                        <p class="font-lexend text-md text-justify">{{ userData["summary"]["summary"] }}</p>
                    </div>
                    <div class="w-full flex flex-col gap-y-5">
                        <h2 class="font-lexend text-3xl text-center">Insights</h2>
                        <p class="font-lexend text-md text-justify">{{ userData["summary"]["insight"] }}</p>
                    </div>
                    <div class="w-full flex flex-col gap-y-5">
                        <h2 class="font-lexend text-3xl text-center">Your Opp</h2>
                        <p class="font-lexend text-md text-justify">{{ userData["summary"]["opp"] }}</p>
                    </div>
                    <h2 class="font-lexend text-2xl text-center text-secondary">CHECK YOUR SPAM! An email with a link to your results (this page) has been sent.</h2>
                    <h2 class="font-lexend text-2xl text-center text-secondary">Re-check this once in a while, new updates will be posted here.</h2>
                    <div class="w-full flex gap-y-4 flex-col mt-10">
                        <h2 class="font-lexend text-2xl text-center">Your Opp? It will be released soon 😉, just be patient.</h2>
                        <h2 class="font-lexend text-2xl text-center">After all, we all need to run on a little hate...</h2>
                        <h2 class="font-lexend text-2xl text-center">or cross the thin line and ask them out for valentines LMFAOO.</h2>
                    </div>
                </div>
            </div>
        </div>
        <!-- <p class="text-white">{{ userData }}</p> -->
    </div>
</template>

<script setup>
const route = useRoute()
const userData = ref(null)
const config = useRuntimeConfig()

const scoreComment = (score)=>{
    if (score < 3333) return "Wow, you are kind of an NPC."
    else if (score >= 3333 && score < 6666) return "Okay icic, you kinda unique."
    else return "Wow, you are quite a character."
}

onMounted(async()=>{
    let data = await fetch(`${config.public.api}/entry/get?uuid=${route.query.uuid}`)
    userData.value = await data.json()
})
</script>