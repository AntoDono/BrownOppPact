<template>
    <div class="h-screen w-full bg-background1 overflow-hidden">
        <div>
            <div ref="strings">

            </div>
            <div class="fixed w-full h-full flex flex-col justify-center items-center gap-y-10 text-white">
                <div>
                    <h1 class="relative font-lexend text-6xl text-center z-20">There is a Thin Line Between</h1>
                    <div>
                        <div class="w-full flex flex-row gap-x-4 items-center justify-center">
                            <h2 class="font-lexend text-5xl text-center">
                                Love
                            </h2>
                            <h2 class="font-lexend text-5xl text-center">
                                Hate
                            </h2>
                            <div ref="redline"
                                class="fixed top-0 h-screen w-[3px] bg-secondary opacity-80 z-10 animate-pulse"></div>
                        </div>
                    </div>
                </div>
                <div class="flex items-center justify-start flex-col z-20">
                    <h2 class="font-urbanist text-3xl text-center">Do Opposites Attract,</h2>
                    <h2 class="font-urbanist text-3xl text-center">Or Will You be Attacked?</h2>
                </div>
                <NuxtLink class="z-20" to="/match">
                    <p class="text-xl font-urbanist font-bold">Form has closed. Try again next year!</p>
                </NuxtLink>
            </div>
        </div>
    </div>
</template>

<script setup>
import gsap from 'gsap';

const horizontal = ref(null)
const vertical = ref(null)
const bowtie = ref(null)
const cover = ref(null)
const redline = ref(null)

</script>

<style>
@keyframes spin {
    0% {
        transform: rotate(0deg);
        opacity: 0.7;
    }

    50% {
        transform: rotate(180deg);
        opacity: 0.15;
    }

    100% {
        transform: rotate(360deg);
        opacity: 0.7;
    }
}

.spin-slow {
    animation: spin 15s linear infinite;
}
</style>