def sum_positive(numbers):
    """คืนค่าผลรวมของตัวเลขที่มากกว่า 0 ในลิสต์"""
    return sum(n for n in numbers if n > 0)