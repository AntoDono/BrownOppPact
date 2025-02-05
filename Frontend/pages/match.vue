<template>
    <div class="h-screen w-screen bg-background1 overflow-y-auto overflow-x-hidden scroll-smooth snap-y snap-mandatory">
        <div
            class="h-screen w-screen flex justify-center items-center min-h-screen pb-10 text-white bg-background1 snap-center snap-always">
            <div class="h-full w-full flex flex-col justify-center items-center">
                <div class="mb-5 w-[10%] min-w-[300px]">
                    <label for="fname" class="block mb-2 text-sm font-medium text-white">First
                        Name</label>
                    <input type="text" v-model="fname"
                        class="outline-none shadow-xs border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500 shadow-xs-light"
                        required />
                </div>
                <div class="mb-5 w-[10%] min-w-[300px]">
                    <label for="lname" class="block mb-2 text-sm font-medium text-white">Last Name</label>
                    <input type="text" v-model="lname"
                        class="outline-none shadow-xs border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500 shadow-xs-light"
                        required />
                </div>
                <div class="mb-5 w-[10%] min-w-[300px]">
                    <label for="class" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Class
                        Of:</label>
                    <select v-model="classof"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                        <option>2029</option>
                        <option selected>2028</option>
                        <option>2027</option>
                        <option>2026</option>
                        <option>2024</option>
                        <option>2023</option>
                        <option>2022</option>
                        <option>2021</option>
                        <option>2020</option>
                    </select>
                </div>
                <div class="mb-5 w-[10%] min-w-[300px]">
                    <label for="gender"
                        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Gender</label>
                    <select v-model="gender"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                        <option disabled>Select gender</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <!-- <option value="helicopter">AttackHelicopter</option> -->
                        <option value="non-binary">Non-binary</option>
                        <option value="transgender">Transgender</option>
                        <option value="genderqueer">Genderqueer</option>
                        <option value="genderfluid">Genderfluid</option>
                        <option value="agender">Agender</option>
                        <option value="other">Other</option>
                        <option value="prefer-not">Prefer not to say</option>
                    </select>
                </div>
                <div class="mb-5 w-[10%] min-w-[300px]">
                    <label for="email" class="block mb-2 text-sm font-medium text-white">Your Brown
                        Email</label>
                    <input type="email" v-model="email" :class="[
                        'shadow-xs border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 outline-none',
                        'text-white focus:ring-blue-500 focus:border-blue-500 shadow-xs-light',
                        isValidEmail ?
                            'border-gray-300 focus:ring-blue-500 focus:border-blue-500' :
                            'border-red-500 focus:ring-red-500 focus:border-red-500'
                    ]" placeholder="...@brown.edu" @input="validateEmail" required />
                    <p v-if="!isValidEmail" class="text-red-500">Invalid Brown University email</p>
                </div>
                <div>
                    <div>
                        <div class="flex items-center mb-4">
                            <input checked id="default-radio-1" type="radio" value="limited" name="default-radio" v-model="shareInformation"
                                class="w-4 h-4 appearance-none border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 
            checked:border-blue-600 relative checked:after:content-[''] checked:after:absolute checked:after:top-1/2 checked:after:left-1/2 
            checked:after:w-2 checked:after:h-2 checked:after:bg-blue-600 checked:after:transform checked:after:-translate-x-1/2 checked:after:-translate-y-1/2">
                            <label for="default-radio-1"
                                class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Share only my initials
                                with my opp.</label>
                        </div>
                        <div class="flex items-center">
                            <input id="default-radio-2" type="radio" value="all" name="default-radio" v-model="shareInformation"
                                class="w-4 h-4 appearance-none border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 
            checked:border-blue-600 relative checked:after:content-[''] checked:after:absolute checked:after:top-1/2 checked:after:left-1/2 
            checked:after:w-2 checked:after:h-2 checked:after:bg-blue-600 checked:after:transform checked:after:-translate-x-1/2 checked:after:-translate-y-1/2">
                            <label for="default-radio-2"
                                class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Share my full name and
                                email with my opp.</label>
                        </div>
                    </div>
                </div>
                <div class="w-full flex flex-col items-center justify-center mt-4 gap-y-2">
                    <p v-if="!basicInfoValid" class="text-red-500">Please fill out all information correctly.</p>
                    <Button1 class="hover:cursor-pointer" @click="submitBasicInformation">
                        <p>Confirm Information</p>
                    </Button1>
                </div>
            </div>
        </div>
        <div v-for="(q, index) in questions"
            class="h-screen w-screen min-h-screen box-content text-white bg-background1 grid grid-rows-[20%_30_40%_10%] snap-center snap-always">
            <div class="w-full h-full flex flex-col items-center justify-center p-4 z-10">
                <h2 class="lg:text-4xl text-xl font-lexend text-center">{{ q["question"] }}</h2>
            </div>
            <div class="w-full h-full flex justify-center items-center z-10">
                <img class="w-[20vw] h-[20vw] min-w-[100px] min-h-[100px] rounded-xl"
                    :src="`${available_images[index >= available_images.length ? index - available_images.length : index]}`" />
            </div>
            <div class="w-full h-full flex justify-center items-start p-4 z-10" v-if="q['type'] == 'slider'">
                <div class="w-fit h-fit flex flex-col gap-y-4">
                    <div class="w-full flex flex-row justify-between font-urbanist text-xl">
                        <p>{{ q["min"]["text"] }}</p>
                        <p>{{ q["max"]["text"] }}</p>
                    </div>
                    <div :id="`qc${q['id']}`" class="w-fit flex flex-row gap-x-2">
                        <div v-for="(i, index) in q['max']['value'] - q['min']['value'] + 1"
                            :id="`qc-child-${q['id']}-${index}`" class="min-h-[40px] min-w-[40px] h-[5vw] w-[5vw] border-3
                            border-gray-300 rounded-lg flex items-center justify-center hover:cursor-pointer hover:scale-[105%] transition-all
                            hover:border-gray-50 duration-300"
                            @click="() => respondQuestion(q['question'], q['id'], q['min']['value'] + (i - 1), i, `qc-child-${q['id']}-${index}`)">
                            <p class="font-urbanist text-lg">{{ i }}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else-if="q['type'] == 'choice'" class="w-full h-full flex justify-center items-center p-4 z-10">
                <div :id="`qc${q['id']}`" class="w-[60%] min-w-[300px] flex flex-col gap-y-2">
                    <div v-for="(choice, index) in q['choices']" :id="`qc-child-${q['id']}-${index}`" class="w-full border-3 border-gray-300 lg:p-4 p-2 rounded-xl
                    hover:cursor-pointer hover:scale-[103%] transition-all hover:border-gray-50 duration-300"
                        @click="() => respondQuestion(q['question'], q['id'], choice['value'], choice['text'], `qc-child-${q['id']}-${index}`)">
                        <p>{{ choice["text"] }}</p>
                    </div>
                </div>
            </div>
            <div v-if="index + 1 == numOfQuestions" class="w-screen h-fit flex justify-center p-4 z-20">
                <Button1 v-if="Object.keys(response).length == numOfQuestions && basicInfoValid" class="hover:cursor-pointer">
                    <p class="text-xl p-2" @click="submit">Find Your Opp</p>
                </Button1>
                <div v-else class="opacity-70">
                    <Button1 class="border-gray-500">
                        <p class="text-xl p-2">Finish All Questions First</p>
                    </Button1>
                </div>
            </div>
            <div class="w-full h-full">
                <!-- THIS IS RESERVED FOR SHOWING FOTTERR THROUGH-->
            </div>
        </div>
        <div ref="loading"
            class="z-30 absolute top-0 left-0 w-full h-full flex justify-center items-center flex-col gap-y-10 bg-background1 hidden">
            <div class="relative flex justify-center items-center">
                <div
                    class="absolute animate-spin rounded-full h-[15vw] w-[15vw] min-w-[150px] min-h-[150px] border-t-4 border-b-4 border-purple-500">
                </div>
                <img src="~assets/images/catloading.jpg"
                    class="rounded-full h-[14vw] w-[14vw] min-w-[140px] min-h-[140px]">
            </div>
            <h2 class="text-white text-xl font-urbanist">Analyzing your response, this might take a few seconds.</h2>
        </div>
    </div>
</template>
<script setup>
const questions = ref([])
const response = ref({})
const isValidEmail = ref(true)
const numOfQuestions = ref(0)
const basicInfoValid = ref(false)
const fname = ref(null)
const lname = ref(null)
const classof = ref(null)
const gender = ref(null)
const email = ref(null)
const shareInformation = ref("limited")
const config = useRuntimeConfig()
const loading = ref(null)
const available_images = ref(['/images/cat-what.png', '/images/gojo.gif', '/images/nihao.png',
    '/images/rat.png', '/images/shooting.jpg', '/images/catthumbs.jpg',
    '/images/thinking.png', '/images/huh.jpg', '/images/flatface.jpg',
    '/images/raiseeyebrow.jpg', '/images/twofinger.jpg', '/images/cool.jpg'])

const router = useRouter()

const submitBasicInformation = () => {
    basicInfoValid.value =
        fname.value != null &&
        lname.value != null &&
        classof.value != null &&
        email.value != null &&
        isValidEmail.value == true &&
        shareInformation.value != null

    if (basicInfoValid.value) { // scroll to questions
        const currentSection = document.querySelector('.snap-center')
        const nextSection = currentSection.nextElementSibling

        if (nextSection) {
            // Scroll to the next section smoothly
            nextSection.scrollIntoView({ behavior: 'smooth' })
        }
    }
}

const validateEmail = () => {
    if (!email.value) {
        isValidEmail.value = true
        return
    }
    isValidEmail.value = email.value.toLowerCase().endsWith('@brown.edu')
}

onMounted(async () => {
    let qs = await $fetch(`${config.public.api}/entry/questions`)
    questions.value = qs.questions
    numOfQuestions.value = Object.keys(questions.value).length
})

const respondQuestion = (question, id, value, user_response, html_choice_id) => {
    id = id.toString()
    response.value[id] = { "question": question, "answer": user_response, "value": value }
    let qc = document.getElementById(`qc${id}`)
    for (let child of qc.children) {
        child.classList.remove('selected')
    }
    document.getElementById(html_choice_id).classList.add("selected")

    setTimeout(() => {
        // Get the current question's container
        const currentQuestion = qc.closest('.snap-center')
        // Get the next question
        const nextQuestion = currentQuestion.nextElementSibling

        if (nextQuestion) {
            // Scroll to the next question smoothly
            nextQuestion.scrollIntoView({ behavior: 'smooth' })
        }
    }, 100) // 300ms delay to show the selection before scrolling
}

const submit = async () => {
    loading.value.classList.remove("hidden")
    try{
        let uuid = await $fetch(`${config.public.api}/entry/create`, {
            method: "POST",
            body: {
                firstname: fname.value,
                lastname: lname.value,
                email: email.value,
                gender: gender.value,
                permission_to_share: shareInformation.value == "all",
                response: response.value
            }
        })
        router.push(`/result?uuid=${uuid}`)
    } catch (error) {
        if (error.response.status == 403){
            alert("Bro, you did this shit before.")
            router.push('/')
        } else{
            alert("Sorry, server error. Try again later.")
        }
    }
}
</script>

<style>
.selected {
    border-color: oklch(38.87% 0.3034 0);
}
</style>