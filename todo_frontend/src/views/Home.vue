<template>
  <div>
    <header class="header">
      <h1 class="header__title">Задачи</h1>
      <add-todo-dialog :categories="listOfCategories"/>
    </header>
    <todo-cards v-bind:cards="allTodos"/>
  </div>
</template>

<script>
import TodoCards from '@/components/TodoCards'
import AddTodoDialog from "@/components/AddTodoDialog"
export default {
  data() {
    return {
      allTodos: [],
      listOfCategories: []
    }
  },
  components: {
    AddTodoDialog,
    TodoCards
  },
  async created() {
    const { data } =
        await this.axios.get('http://localhost:8000/api/v1/todos/')
    this.allTodos = data
    this.listOfCategories = this.allTodos.map(c => c.title)
  }
}
</script>

<style scoped>
  .header {
    background-color: #61acd7;
    color: #fff;
    padding: 20px 0px;
  }
  .header__title {
    font-size: 32px;
  }
</style>

