document.getElementById('recommendBtn').addEventListener('click', function () {
    const recommendations = [
      "Try 'Let Me Down Slowly' by Alec Benjamin 🎵",
      "Listen to 'Perfect' by Ed Sheeran 💖",
      "How about 'Believer' by Imagine Dragons 🔥",
      "Feel the vibe with 'Levitating' by Dua Lipa ✨"
    ];
  
    const randomIndex = Math.floor(Math.random() * recommendations.length);
    document.getElementById('recommendation').textContent = recommendations[randomIndex];
  });
  