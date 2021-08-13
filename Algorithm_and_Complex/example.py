def hanoi(n, src, dst, tmp):
  if n > 0:
    hanoi(n-1, src, tmp, dst)
    print(f"Move disk {n} from {src} to {dst}")
    hanoi(n-1, tmp, dst, src)
    
hanoi(4, 'A', 'C', 'B')