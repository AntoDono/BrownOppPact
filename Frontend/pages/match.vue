<template>
    <div class="h-screen w-screen bg-background1 overflow-y-auto overflow-x-hidden scroll-smooth snap-y snap-mandatory">
        <div
            class="h-screen w-screen flex justify-center items-center min-h-screen text-white bg-background1 snap-center snap-always">
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
                        <option value="">Select gender</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="helicopter">AttackHelicopter</option>
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
                <p v-if="!basicInfoValid" class="text-red-500 mb-4">Please fill out all information correctly.</p>
                <Button1 class="hover:cursor-pointer" @click="submitBasicInformation">
                    <p>Confirm Information</p>
                </Button1>
            </div>
        </div>
        <div v-for="(q, index) in questions"
            class="h-screen w-screen min-h-screen text-white bg-background1 grid grid-rows-[40%_50_10%] snap-center snap-always">
            <div class="w-full h-full flex flex-col items-center justify-center p-8">
                <h2 class="text-4xl font-playfair text-center">{{ q["question"] }}</h2>
            </div>
            <div class="w-full h-full flex justify-center items-center p-4" v-if="q['type'] == 'slider'">
                <div class="w-fit h-fit flex flex-col gap-y-4">
                    <div class="w-full flex flex-row justify-between font-nunito text-xl">
                        <p>{{ q["min"]["text"] }}</p>
                        <p>{{ q["max"]["text"] }}</p>
                    </div>
                    <div :id="`qc${q['id']}`" class="w-fit flex flex-row gap-x-2">
                        <div v-for="(i, index) in q['max']['value'] - q['min']['value'] + 1"
                            :id="`qc-child-${q['id']}-${index}`" class="min-h-[40px] min-w-[40px] h-[4vw] w-[4vw] border-3
                            border-gray-300 rounded-lg flex items-center justify-center hover:cursor-pointer hover:scale-[105%] transition-all
                            hover:border-gray-50 duration-300"
                            @click="() => respondQuestion(q['question'], q['id'], q['min']['value'] + (i - 1), i, `qc-child-${q['id']}-${index}`)">
                            <p class="font-nunito text-[3vmin]">{{ i }}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else-if="q['type'] == 'choice'" class="w-full h-full flex justify-center items-center p-4">
                <div :id="`qc${q['id']}`" class="w-[60%] min-w-[300px] flex flex-col gap-y-4">
                    <div v-for="(choice, index) in q['choices']" :id="`qc-child-${q['id']}-${index}`" class="w-full border-3 border-gray-300 p-4 rounded-xl
                    hover:cursor-pointer hover:scale-[103%] transition-all hover:border-gray-50 duration-300"
                        @click="() => respondQuestion(q['question'], q['id'], choice['value'], choice['text'], `qc-child-${q['id']}-${index}`)">
                        <p>{{ choice["text"] }}</p>
                    </div>
                </div>
            </div>
            <div v-if="index + 1 == numOfQuestions" class="w-screen h-fit flex justify-center">
                <Button1 v-if="Object.keys(response).length == numOfQuestions" class="hover:cursor-pointer">
                    <p class="text-xl p-2" @click="submit">Find Your Opp</p>
                </Button1>
                <div v-else class="opacity-70">
                    <Button1 class="border-gray-500">
                        <p class="text-xl p-2">Finish All Questions First</p>
                    </Button1>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
const questions = ref([])
const response = ref({})
const isValidEmail = ref(true)
const numOfQuestions = ref(0)
const basicInfoValid = ref(true)
const fname = ref(null)
const lname = ref(null)
const classof = ref(null)
const gender = ref(null)
const email = ref(null)

const submitBasicInformation = () => {
    basicInfoValid.value =
        fname.value != null &&
        lname.value != null &&
        classof.value != null &&
        email.value != null &&
        isValidEmail.value == true

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
    let qs = await $fetch("http://localhost:8000/entry/questions")
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

const submit = async() => {
    let res = await $fetch("http://localhost:8000/entry/create", {
        method: "POST",
        body: {
            firstname: fname.value,
            lastname: lname.value,
            email: email.value,
            response: response.value
        }
    })
}
</script>

<style>
.selected {
    border-color: oklch(38.87% 0.3034 0);
}
</style>