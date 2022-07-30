cross_tab_prop.plot(kind='bar',
                    stacked=True,
                    colormap='tab10',
                    figsize=(10, 6))

plt.legend(loc="upper left", ncol=2)
plt.xlabel("Release Year")
plt.ylabel("Proportion")

for n, x in enumerate([*cross_tab.index.values]):
    for proportion in cross_tab_prop.loc[x]:
        plt.text(x=n,
                 y=proportion,
                 s=f'{np.round(proportion * 100, 1)}%',
                 color="black",
                 fontsize=12,
                 fontweight="bold")

plt.show()