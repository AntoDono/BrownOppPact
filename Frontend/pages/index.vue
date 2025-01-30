<template>
    <div class="h-screen w-full bg-background1 overflow-hidden">
        <div>
            <div ref="strings">
                <div v-for="index in 20" 
                     class="fixed top-0 border-2 border-pink-800 w-screen h-screen origin-center spin-slow opacity-20" 
                     :class="`rotate-${18 * index}`"
                     :style="{
                         animationDelay: `${-0.75 * index}s`
                     }">
                </div>
            </div>
            <div class="fixed w-full h-full flex flex-col justify-center items-center gap-y-10 text-white">
                <div>
                    <h1 class="font-playfair text-5xl text-center">There is a Thin Line Between</h1>
                    <h2 class="font-playfair text-5xl text-center">
                        Love and Hate
                    </h2>
                </div>
                <div class="flex items-center justify-start flex-col">
                    <h2 class="font-nunito text-3xl">Does Opposite Attract,</h2>
                    <h2 class="font-nunito text-3xl">Or Are You Going to Get Whacked?</h2>
                </div>
            </div>
        </div>
        <div ref="cover" class="fixed top-0 left-0 bg-background2 w-full h-full">
            <div ref="horizontal" class="fixed w-screen">
                <div class="w-full h-8 bg-primary"></div>
                <div class="w-full h-8 bg-secondary"></div>
            </div>
            <div ref="vertical" class="fixed h-screen flex flex-row">
                <div class="h-full w-8 bg-primary"></div>
                <div class="h-full w-8 bg-secondary"></div>
            </div>
            <img ref="bowtie" src="~assets/images/bow.png" class="w-64"/>
        </div>
    </div>
</template>

<script setup>
import gsap from 'gsap';
import * as PIXI from "pixi.js"

const horizontal = ref(null)
const vertical = ref(null)
const bowtie = ref(null)
const cover = ref(null)
const canvas = ref(null)

onMounted(async()=>{
    gsap.set(horizontal.value, {
        translateY: `${0.5 * (window.innerHeight - horizontal.value.offsetHeight)}px`
    }) 

    gsap.set(vertical.value, {
        translateX: `${0.5 * (window.innerWidth - vertical.value.offsetWidth)}px`
    })

    gsap.set(bowtie.value, {
        translateX: `${0.5 * (window.innerWidth - bowtie.value.offsetWidth)}px`,
        translateY: `${0.5 * (window.innerHeight - bowtie.value.offsetHeight)}px`
    }) 

    const timeline = gsap.timeline()

    timeline.to(bowtie.value, {
        delay: 1.5,
        scale: 0,
        duration: 1.5,
        ease: "bounce.inOut",
        display: "none"
    })
    
    timeline.to(vertical.value, {
        delay: 0.3,
        duration: 0.7,
        y: window.innerHeight,
        ease: "expoScale(0.5,7,none)",
        display: "none"
    })

    timeline.to(horizontal.value, {
        delay: 0.3,
        duration: 0.7,
        x: window.innerWidth,
        ease: "expoScale(0.5,7,none)",
        display: "none"
    })

    timeline.to(cover.value, {
        delay: 0.5,
        scaleY: -1,
        y: window.innerHeight,
        alpha: 0,
        display: "none"
    })

})
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

.spin-slow{
    animation: spin 15s linear infinite;
}



</style>