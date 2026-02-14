function addUser() {
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;

    fetch("/add_user", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            email: email
        })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}

function loadUsers() {
    fetch("/get_users")
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById("userList");
        list.innerHTML = "";

        data.forEach(user => {
            const li = document.createElement("li");
            li.textContent = user.username + " - " + user.email;
            list.appendChild(li);
        });
    });
}
