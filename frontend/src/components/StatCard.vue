<template>
  <div class="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6">
    <div class="flex items-center justify-between">
      <div>
        <p class="text-sm text-text-muted-light dark:text-text-muted-dark">{{ label }}</p>
        <p class="text-3xl font-bold text-text-light dark:text-text-dark mt-2">{{ value }}</p>
        <p v-if="change" class="text-sm mt-2" :class="changeClass">
          <span class="material-symbols-outlined text-xs align-middle">{{ changeIcon }}</span>
          {{ change }}
        </p>
      </div>
      <div class="w-12 h-12 rounded-lg flex items-center justify-center" :class="iconBgClass">
        <span class="material-symbols-outlined text-2xl" :class="iconClass">{{ icon }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StatCard',
  props: {
    label: {
      type: String,
      required: true
    },
    value: {
      type: [String, Number],
      required: true
    },
    icon: {
      type: String,
      required: true
    },
    change: {
      type: String,
      default: ''
    },
    trend: {
      type: String,
      default: 'neutral', // 'up', 'down', 'neutral'
      validator: (value) => ['up', 'down', 'neutral'].includes(value)
    }
  },
  computed: {
    iconBgClass() {
      return 'bg-primary/10'
    },
    iconClass() {
      return 'text-primary'
    },
    changeClass() {
      if (this.trend === 'up') return 'text-green-600 dark:text-green-400'
      if (this.trend === 'down') return 'text-red-600 dark:text-red-400'
      return 'text-text-muted-light dark:text-text-muted-dark'
    },
    changeIcon() {
      if (this.trend === 'up') return 'trending_up'
      if (this.trend === 'down') return 'trending_down'
      return 'remove'
    }
  }
}
</script>
