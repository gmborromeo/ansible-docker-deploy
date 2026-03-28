const express = require('express')
const app = express()

app.get('/', (req, res) => {
    res.send(`
        <h1> Node.js App</h1>
        <p> Deployed automaticall with Ansible + Docker!</p1>
        `)
})

app.listen(3000, '0.0.0.0', () => {
    console.log('Node.js app is running on port 3000')
})