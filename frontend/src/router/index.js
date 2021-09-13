import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Element from '@/components/Element'
import Test from '@/components/Test'
import NavMenu from '@/components/NavMenu'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/element',
      name: 'Element',
      component: Element
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
    {
      path: '/nav',
      name: 'NavMenu',
      component: NavMenu
    },
  ]
})
