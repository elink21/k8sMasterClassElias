# Challenge 2: Pods 
---

### 1. Pod definition
[code](pod.yaml)

```
apiVersion: v1

kind: Pod

metadata:
  name: challenge1pod
  labels:
    environment: development
    app: roxsross

spec:
  containers:
  - name: challenge1container
    image: roxsross12/k8s_test_web:latest
    ports:
    - containerPort: 80
```

### 2. Pod creation

![image1.png](imagen1.png)

### 3. Pod description

![image2.png](imagen2.png)

### 4. Inspecting pod contents

![image3.png](imagen3.png)

### 5. Accesing webpage through the browser using port-forwarding

![image4.png](imagen4.png)

### 6. Checking logs from the pod

![image5.png](imagen5.png)
