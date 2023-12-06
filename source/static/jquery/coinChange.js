function solveCoinChange() {
    const amount = parseInt(document.getElementById('amount').value);
    const coins = document.getElementById('coins').value.split(',').map(coin => parseInt(coin));

    if (isNaN(amount) || coins.some(isNaN)) {
      alert('Please enter valid numbers');
      return;
    }

    const result = coinChange(amount, coins);
    visualizeCoinChange(result);
  }

  function coinChange(amount, coins) {
    const dp = Array(amount + 1).fill(Infinity);
    const coinUsed = Array(amount + 1).fill(null);
    dp[0] = 0;

    for (const coin of coins) {
      for (let i = coin; i <= amount; i++) {
        if (dp[i - coin] + 1 < dp[i]) {
          dp[i] = dp[i - coin] + 1;
          coinUsed[i] = coin;
        }
      }
    }

    const result = [];
    let currentAmount = amount;
    while (currentAmount > 0) {
      result.push(coinUsed[currentAmount]);
      currentAmount -= coinUsed[currentAmount];
    }

    return result.reverse();
  }

  function visualizeCoinChange(coinsUsed) {
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
      const renderer = new THREE.WebGLRenderer();
      renderer.setSize(window.innerWidth, window.innerHeight);
      document.body.appendChild(renderer.domElement);
    
      // Add a directional light to illuminate the coins
      const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
      directionalLight.position.set(1, 1, 1).normalize();
      scene.add(directionalLight);
    
      // Add ambient light to brighten the scene
      const ambientLight = new THREE.AmbientLight(0x404040); 
      scene.add(ambientLight);
    
      let xPosition = -50;
    
      for (const coin of coinsUsed) {
        const radius = 10;
        const height = coin * 2;
    
        const geometry = new THREE.CylinderGeometry(radius, radius, height, 32);
        const material = new THREE.MeshStandardMaterial({ color: 0xf1c40f });
    
        const coinMesh = new THREE.Mesh(geometry, material);
    
        coinMesh.position.set(xPosition, height / 2, 0);
        scene.add(coinMesh);
    
        xPosition += 30;
      }
    
      camera.position.z = 70;
    
      const animate = function () {
        requestAnimationFrame(animate);
    
        // Rotate the coins
        scene.children.forEach(coinMesh => {
          coinMesh.rotation.x += 0.01;
          coinMesh.rotation.y += 0.01;
        });
    
        renderer.render(scene, camera);
      };
    
      animate();
    }