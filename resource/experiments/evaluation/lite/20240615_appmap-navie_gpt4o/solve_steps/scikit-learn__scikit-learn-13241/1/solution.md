<change>
<file change-number-for-this-file="1">sklearn/decomposition/kernel_pca.py</file>
<original line-count="14" no-ellipsis="true"><![CDATA[
        # sort eigenvectors in descending order
        indices = self.lambdas_.argsort()[::-1]
        self.lambdas_ = self.lambdas_[indices]
        self.alphas_ = self.alphas_[:, indices]

        # remove eigenvectors with a zero eigenvalue
        if self.remove_zero_eig or self.n_components is None:
            self.alphas_ = self.alphas_[:, self.lambdas_ > 0]
            self.lambdas_ = self.lambdas_[self.lambdas_ > 0]

        return K
]]></original>
<modified no-ellipsis="true"><![CDATA[
        # sort eigenvectors in descending order
        indices = self.lambdas_.argsort()[::-1]
        self.lambdas_ = self.lambdas_[indices]
        self.alphas_ = self.alphas_[:, indices]

        # normalize signs of eigenvectors
        for i in range(self.alphas_.shape[1]):
            if np.abs(self.alphas_[:, i]).max() > 0:
                self.alphas_[:, i] *= np.sign(self.alphas_[:, i].max())
                
        # remove eigenvectors with a zero eigenvalue
        if self.remove_zero_eig or self.n_components is None:
            self.alphas_ = self.alphas_[:, self.lambdas_ > 0]
            self.lambdas_ = self.lambdas_[self.lambdas_ > 0]

        return K
]]></modified>
</change>