<template>
    <div class="overflow-visible">
        <a :href="destination" target="_blank">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                <title>{{alt}}</title>
                <slot/>
            </svg>
        </a>
    </div>
</template>

<script>

export default {
    name: "socialMedia",
    setup() {
        
    },
    props:{
        alt: {
            type: String,
            default: "/"
        },
        destination: {
            type: String,
            default: "/"
        }
    },
}

</script>

<style scoped>

svg{
    fill: var(--color-background3);
    transition: all ease 0.3s;
}

svg:hover {
    fill: var(--color-background2);
    transform: translateY(-0.45em);
}

</style>