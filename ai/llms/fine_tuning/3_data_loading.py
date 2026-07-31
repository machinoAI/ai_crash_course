"""
1. Why do we shuffle the training data?
    - Shuffling prevents the model from learning the order of the data.
    - It improves generalization, reduces bias, and helps gradient descent converge more reliably.

2. What is a Stratified Split?
    - A stratified split preserves the class distribution across train, validation, and test datasets.
    - It is mainly used for classification tasks with imbalanced classes.
3. What is a DataLoader?
    - A DataLoader reads samples from a Dataset and efficiently creates mini-batches for training.
    - It also supports shuffling, multiprocessing, and prefetching.

4. Why do we use Mini-Batches?
    - Processing the entire dataset at once is memory-intensive, while one sample at a time is inefficient.
    - Mini-batches balance GPU utilization, memory usage, and gradient stability.

5. What is Batch Size?
    - Batch size is the number of training examples processed in one forward and backward pass before updating the model weights.

 6. What is Effective Batch Size?
    - Effective batch size is the total number of samples contributing to one optimizer update, considering gradient accumulation and distributed training.

    Effective Batch Size

        = Batch Size × Gradient Accumulation Steps × Number of GPUs

7. What is Gradient Accumulation?
    - Gradient accumulation computes gradients over multiple mini-batches before performing a single optimizer step. It simulates a larger batch size without increasing GPU memory.

8. Why do we use Gradient Accumulation?
    - It enables training with large effective batch sizes on memory-constrained GPUs while maintaining training stability.

9. What are DataLoader Workers (num_workers)?
    - num_workers specifies how many CPU processes load and preprocess data in parallel while the GPU is training.
    - Increasing workers can reduce data loading bottlenecks.

10. What is pin_memory=True?
    pin_memory=True allocates page-locked (pinned) CPU memory, allowing faster data transfer from CPU to GPU. It is beneficial when training on CUDA GPUs.


"""