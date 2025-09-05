<template>
  <div id="app">
    <h1>🎬 Movie Project</h1>
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/movies">Movies</router-link> |
      <router-link to="/review-search">Review Search</router-link> |
      <router-link to="/recommended">Recommended</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style>
nav {
  margin-bottom: 20px;
}
</style>
