<template>
  <div class="add__btn">
    <v-btn
        icon
        elevation="1"
        @click="toggleDialog">
      <v-icon
          color="#fff"
      >mdi-plus</v-icon>
    </v-btn>
    <v-dialog v-model="dialog" max-width="600px">
      <v-card>
        <v-card-title class="dialog__title">
            <h2>Новая Задача</h2>
          <v-spacer></v-spacer>
          <v-icon class="close__btn" @click="toggleDialog">mdi-close</v-icon>
        </v-card-title>
        <v-card-text class="task__name">
          <v-text-field
              v-model="payload.text"
              label="Название задачи"
              outlined
              clearable/>
        </v-card-text>
        <v-card-text class="category__name">
           <v-combobox
            :items="categories"
            v-model="payload.title"
            :search-input.sync="payload.title"
            label="Категория"
            outlined
            clearable
            hide-selected
          ></v-combobox>
        </v-card-text>
        <v-card-actions class="submit__btn">
          <v-btn
              color="#61acd7"
              elevation="2"
              @click="sendNewTask"
          >Создать</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
const payload =  {
  text: '',
  title: ''
}
export default {
  name: 'AddTodoDialog',
  props: {
    categories: {
      type: Array,
      default: () => []
    }
  },
  data () {
    return {
      payload: { ...payload },
      dialog: false
    }
  },
  methods: {
    toggleDialog () {
      this.dialog = !this.dialog
      this.payload = { ...payload }
    },
    async sendNewTask () {
      const { data } =
          await this.axios.post('http://localhost:8000/api/v1/todos/', {
            ...this.payload
          })
      this.toggleDialog()
    }
  }
}
</script>

<style scoped>
.add__btn {
  position: absolute;
  right: 25px;
  top: 26px;
}
.v-dialog>.v-card> .dialog__title {
  border-bottom: 1px solid #dedede;
}
.v-dialog>.v-card> .task__name {
  margin-top: 15px;
  padding-bottom: 0px;
}
.v-dialog>.v-card> .category__name {
  padding-bottom: 0px;
}
.v-dialog>.v-card> .submit__btn {
  display: flex;
  justify-content: center;
  padding-bottom: 20px;
}
.v-dialog>.v-card> .submit__btn button {
  color: #fff;
  padding: 15px;
}
</style>