import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Element from '@/components/Element'
import Test from '@/components/Test'
import MainDefault from '@/components/MainDefault'


Vue.use(Router)

export default new Router({
  routes: [

    {
      path: '/element',
      name: 'Element',
      component: Element
    },
    {
      path: '/',
      name: 'MainDefault',
      component: MainDefault
    },
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/test',
      name: 'Test',
      component: Test
    },
  ]
})
