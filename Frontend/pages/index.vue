<template>
    <div class="h-screen w-full bg-background1 overflow-hidden">
        <div>
            <svg width="100%" height="100%">
                <path d="M0,150 Q300,100 600,150 T1200,150" stroke="red" stroke-width="3" fill="none" />
            </svg>
            <div class="text-white">
                <h1 class="font-playfair text-6xl">There is a Thin Line Between and Hate</h1>
                <h2 class="font-nunito text-2xl">Does Opposite Attract,</h2>
                <h2 class="font-nunito text-2xl">Or Are You Going to Get Whacked?</h2>
            </div>
        </div>
        <div ref="cover" class="fixed top-0 left-0 bg-background2 w-full h-full">
            <div ref="horizontal" class="fixed w-screen">
                <div class="w-full h-4 bg-primary"></div>
                <div class="w-full h-4 bg-secondary"></div>
            </div>
            <div ref="vertical" class="fixed h-screen flex flex-row">
                <div class="h-full w-4 bg-primary"></div>
                <div class="h-full w-4 bg-secondary"></div>
            </div>
            <img ref="bowtie" src="~assets/images/bow.png" class="w-32"/>
        </div>
    </div>
</template>

<script setup>
import gsap from 'gsap';

const horizontal = ref(null)
const vertical = ref(null)
const bowtie = ref(null)
const cover = ref(null)

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

    const app = new PIXI.Application({ width: window.innerWidth, height: window.innerHeight, transparent: true });
    this.$refs.canvasContainer.appendChild(app.view);

    const graphics = new PIXI.Graphics();
    graphics.lineStyle(3, 0xff0000, 1);
    graphics.moveTo(0, 150);

    for (let i = 0; i < window.innerWidth; i += 100) {
      graphics.quadraticCurveTo(i + 50, Math.random() * 100 + 100, i + 100, 150);
    }

    app.stage.addChild(graphics);
})
</script>