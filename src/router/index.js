import Vue from 'vue';
import Router from 'vue-router';
import Index from '@/components/views/Index';
import About from '@/components/views/About';
import Contact from '@/components/views/Contact';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index,
    },
    {
      path: '/about',
      name: 'About',
      component: About,
    },
    {
      path: '/contact',
      name: 'Contact',
      component: Contact,
    },
  ],
});
