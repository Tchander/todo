<template>
  <div v-bind="$attrs">
    <h2 class="card__title">{{ card.title }}</h2>
    <ul>
      <li
          class="card__content"
          v-for="(todo, i) of card.todos"
      >
        <input
            class="card__checkbox"
            type="checkbox"
            v-model=todo.isCompleted
            v-on:click="changeIsCompleted(todo)"
        >
        <div v-if="!todo.isCompleted">
          <div class="card__text"
             style="text-decoration: none">{{ todo.text }}</div>
        </div>
        <div v-else>
          <div class="card__text"
             style="text-decoration: line-through">{{ todo.text }}</div>
        </div>
         <v-icon class="delete__todo" @click="deleteTodo(todo)">mdi-close</v-icon>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    card: {
      type: Object,
      required: true,
      default: () => ({})
    },
    index: Number
  },
  data() {
    return {
      selectedTodo: [],
      cardId: Number
    }
  },
  methods: {
    async changeIsCompleted(todo) {
      this.selectedTodo = {...todo}
      const isCompleted = !this.selectedTodo.isCompleted
      const { data } =
        await axios.patch(
            `http://localhost:8000/api/v1/todos/${todo.id}/`, {
              isCompleted
        })
    },
    async deleteTodo(todo) {
      console.log(todo)
      const { data } =
      await axios.delete(`http://localhost:8000/api/v1/todos/${todo.id}/`)
    }
  }
}
</script>

<style scoped>
.card__title {
  font-size: 24px;
  font-weight: 500;
  text-align: start;
  border-bottom: 1px solid #dedede;
  padding-bottom: 10px;
}
ul {
  text-align: start;
  margin-top: 10px;
}
.card__content {
  list-style-type: none;
  padding-left: 5px;
  display: flex;
  align-items: center;
  margin-bottom: 14px;
  position: relative;
}
.card__checkbox {
  width: 20px;
  height: 20px;
  margin-right: 14px;
}
.card__content .delete__todo {
  position: absolute;
  right: 0;
  cursor: pointer;
}
</style>