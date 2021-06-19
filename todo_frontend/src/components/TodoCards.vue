<template>
  <div class="todo__container">
    <div class="todo__cards">
      <todo-item
        class="todo__card"
        v-for="(card, i) of cards" :key="card.id"
        v-bind:card="card"
        v-bind:index="i"
      />
    </div>
  </div>
</template>

<script>
import TodoItem from '@/components/TodoItem'
export default {
  props: ['cards'],
  components: {
    TodoItem
  },
}
</script>

<style>
.todo__container {
  width: 100%;
  max-width: 1440px;
  margin: 0 auto;
}
.todo__cards {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
}
.todo__card {
  width: 33%;
  margin: 30px 5px;
  padding: 10px;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.75);
}
</style>